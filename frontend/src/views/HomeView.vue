<template>
  <div class="home">
    <div class="header">
      <img alt="Your Logo" src="../assets/logo.png" class="logo" />
      <iframe
        id="soundcloudWidget"
        width="100%"
        height="100"
        scrolling="no"
        frameborder="no"
        :src="initialWidgetUrl"
      ></iframe>
    </div>
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
/* global SC */
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  data () {
    return {
      trackID: '465237561', // 초기 SoundCloud ID
      initialWidgetUrl: ''
    }
  },
  mounted () {
    this.initialWidgetUrl = `https://w.soundcloud.com/player/?url=https://api.soundcloud.com/tracks/${this.trackID}`
    setTimeout(() => {
      const widget = SC.Widget(document.getElementById('soundcloudWidget'))
      widget.load(`https://api.soundcloud.com/tracks/${this.trackID}`, {
        auto_play: true,
        buying: false,
        sharing: false,
        show_artwork: false,
        show_playcount: false
      })
    }, 1000)
  }
}
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100px; /* 높이는 원하는 대로 조절하세요. */
  margin-bottom: 20px;
}

.logo {
  margin-right: 20px; /* 로고와 SoundCloud 플레이어 사이의 간격을 조정하세요. */
}

.soundcloud-player {
  width: 70%; /* 필요한 경우 플레이어의 너비를 조절하세요. */
}
</style>
