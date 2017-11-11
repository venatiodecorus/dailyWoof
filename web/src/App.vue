<template>
  <div id="app">
    <LandingPage />
    <button v-on:click="getStories">Get Stories</button>
    <Story
        v-for="story in stories"
        v-bind:image="story.image"
        v-bind:title="story.title"
        v-bind:description="story.description"
        v-bind:story="story.story"
    />
  </div>
</template>

<script>
import axios from 'axios';
import LandingPage from './components/Landing';
import Story from './components/Story';

export default {
  name: 'app',
  components: {
    LandingPage,
    Story,
  },
  data() {
    return {
      stories: [],
    };
  },
  created() {
    this.getStories();
  },
  methods: {
    async getStories() {
      const res = await axios.get('/stories');
      this.stories = this.stories.concat(res.data.data);
    },
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
