<template>
    <div class="story">
        <img class="small" v-bind:src="image">
        <h3>{{ title }}</h3>
        <p class="description">{{ description }}</p>
        <button v-if="!showStory" v-on:click="show"> More </button>
        <p v-if="showStory" class="story">{{ story }}</p>

    </div>
</template>

<script>
export default {
  name: 'Story',
  props: [
    'image',
    'title',
    'description',
    'story',
  ],
  data: () => ({ showStory: false }),
  methods: {
    show() {
      this.showStory = !this.showStory;
    },
  },
};
</script>

<style scoped>
 h1, h2 {
     font-weight: normal;
 }

 a {
     color: #42b983;
 }
 .small {
     width: 50%;
 }
</style>
