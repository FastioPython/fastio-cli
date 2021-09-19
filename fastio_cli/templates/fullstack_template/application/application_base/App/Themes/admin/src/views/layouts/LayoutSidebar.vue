
<template v-slot:prepend>
  <v-list>
    <v-list-item two-line>
        <v-list-item-avatar>
          <img src="../../../public/logo.png">
        </v-list-item-avatar>

        <v-list-item-content>
        <v-list-item-title>
          <h2>PyWorks</h2>
        </v-list-item-title>
        <!-- <v-list-item-subtitle>Super Admin</v-list-item-subtitle> -->
        </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item
        v-for="item in items"
        :key="item.title"
        link
        @click="$router.push({ path: item.route })"
    >
        <v-list-item-icon>
        <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
        <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: 'LayoutSidebar',
  data: () => ({
    items: [
      { title: 'Dashboard', icon: 'mdi-view-dashboard', route: '/' },
      { title: 'Users', icon: 'mdi-account-group-outline', route: '/users' },
      { title: 'Setting', icon: 'mdi-settings', route: '/users' }
    ]
  })
}
</script>
