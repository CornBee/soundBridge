from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager

async def get_soundcloud_track_id(url: str):
    # 드라이버 설정 및 URL 열기
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url + "/popular-tracks")
    
    try:
        # 'Share' 버튼 클릭
        share_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@title, 'Share')]"))
        )
        share_button.click()

        # 페이지 소스 가져오기
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 'Embed' 탭에서 iframe 코드 찾기
        embed_tab = soup.find("a", class_="tabs__tab g-tabs-link", string="Embed")
        iframe_input = None
        if embed_tab:
            iframe_input = embed_tab.find_next("input", class_="widgetCustomization__textInput widgetCustomization__widgetCode")

        # iframe 코드에서 트랙 ID 추출
        if iframe_input:
            iframe_src = iframe_input.get("value", "")
            track_id = iframe_src.split("/tracks/")[1].split("&")[0] if "/tracks/" in iframe_src else None
            return {"track_id": track_id}
        else:
            return {"error": "Embed info not found."}

    finally:
        driver.quit()