from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models import User
from database import SessionLocal
import time
import re

def get_soundcloud_track_id(url: str):
    # 드라이버 설정 및 URL 열기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument(f'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.path = '../usr/src/chrome/chromedriver'

    driver = webdriver.Chrome(options)
    driver.get(url + "/popular-tracks")
    
    try:
        time.sleep(1)
        # 'I Accept' 버튼 클릭
        accept_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@id, 'onetrust-accept-btn-handler') and contains(text(), 'I Accept')]"))
        )
        accept_button.click()

        # 'Share' 버튼 클릭
        # 예시: 특정 클래스를 가진 'Share' 버튼만 찾기
        share_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@title, 'Share') and contains(@class, 'sc-button-small')]"))
        )
        share_button.click()    
        time.sleep(1)

        # 'Embed' 탭 클릭
        embed_tab = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'g-tabs-link') and contains(text(), 'Embed')]"))
        )   
        embed_tab.click()

        time.sleep(1)
        # 원하는 코드를 찾습니다.
        code = driver.find_element(By.CLASS_NAME, "widgetCustomization__textInput")

        # 코드의 값 가져오기
        copied_text = code.get_attribute('value')
        match = re.search(r"/tracks/(\d+)", copied_text)
        if match:
            track_id = match.group(1)
            return track_id
        else:
            print("Track ID not found.")


    finally:
        driver.quit()

def update_soundcloud_track_id(user_id: int, track_id: int):
    """Updates the soundcloud_track_id for a specific user in the database."""
    # Create a new session
    session = SessionLocal()

    try:
        # Query the user by user_id
        user = session.query(User).filter(User.user_id == user_id).one_or_none()
        if not user:
            print(f"No user found with id {user_id}")
            return

        # Update the user's soundcloud_track_id
        user.soundcloud_track_id = track_id

        # Commit the changes
        session.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()

    finally:
        session.close()

