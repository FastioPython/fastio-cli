<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app dark class="teal"
    >
      <LayoutSidebar/>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <LayoutNavbar/>
    </v-app-bar>

    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid class="px-5">
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import LayoutSidebar from '@/views/layouts/LayoutSidebar'
import LayoutNavbar from '@/views/layouts/LayoutNavbar'

export default {
  data: () => ({
    drawer: null,
    items: [
      { title: 'Dashboard', icon: 'mdi-view-dashboard' },
      { title: 'My Account', icon: 'mdi-account' },
      { title: 'Users', icon: 'mdi-account-group-outline' }
    ]
  }),
  components: {
    LayoutSidebar,
    LayoutNavbar
  }
}
</script>
