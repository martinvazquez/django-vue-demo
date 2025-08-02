<template> 
  <div>
    <a href="#" @click.prevent="showCats">Show cats</a>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Color</th>
          <th>Age</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="cat in cats" :key="cat.id">
          <td>{{ cat.name }}</td>
          <td>{{ cat.color }}</td>
          <td>{{ cat.age }}</td>
        </tr>
      </tbody>

    </table>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { getCats } from './services/getCats'; 

  let cats = ref([]);

  const showCats = () => {
    getCats().then(
      (data) => {
        cats.value = data
      }
    )
  }
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
