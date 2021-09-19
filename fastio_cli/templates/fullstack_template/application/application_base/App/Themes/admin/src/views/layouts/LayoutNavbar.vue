<template>
  <v-container>
    <v-row>
      <v-col cols="7">
        <v-row>
          <v-toolbar-title class="my-3"></v-toolbar-title>
        </v-row>
      </v-col>

      <v-col cols="5">
        <v-row justify="end">
          <v-badge :content="messages" :value="messages" color="error" overlap class="my-2">
            <v-icon large>mdi-message-text</v-icon>
          </v-badge>
          <div class="mx-3"></div>
          <v-menu
            v-model="menu"
            :close-on-content-click="false"
            :nudge-width="200"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn icon fab class="p-0" v-bind="attrs" v-on="on">
                <v-avatar size="40">
                  <v-img src="https://avatars3.githubusercontent.com/u/46224928?s=460&u=d42fda2f2329da92494d01c8dda613c5887f0309&v=4"></v-img>
                </v-avatar>
              </v-btn>
            </template>

            <v-card>
              <v-list>
                <v-list-item>
                  <v-list-item-avatar>
                    <img src="https://avatars3.githubusercontent.com/u/46224928?s=460&u=d42fda2f2329da92494d01c8dda613c5887f0309&v=4" alt="Alexander"/>
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <v-list-item-title>Alexander</v-list-item-title>
                    <v-list-item-subtitle>Creator of PyWorks</v-list-item-subtitle>
                  </v-list-item-content>

                  <v-list-item-action>
                    <v-btn
                      :class="fav ? 'red--text' : ''"
                      icon
                      @click="fav = !fav"
                    >
                      <v-icon>mdi-heart</v-icon>
                    </v-btn>
                  </v-list-item-action>
                </v-list-item>
              </v-list>

              <v-divider></v-divider>

              <v-list>
                <v-list-item>
                  <v-list-item-action>
                    <v-switch v-model="message" color="purple"></v-switch>
                  </v-list-item-action>
                  <v-list-item-title>Enable messages</v-list-item-title>
                </v-list-item>

                <v-list-item>
                  <v-list-item-action>
                    <v-switch v-model="hints" color="purple"></v-switch>
                  </v-list-item-action>
                  <v-list-item-title>Enable hints</v-list-item-title>
                </v-list-item>
              </v-list>

              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn text @click="menu = false"> Cancel </v-btn>
                <v-btn color="primary" text @click="menu = false"> Save </v-btn>
              </v-card-actions>
            </v-card>
          </v-menu>
          <!-- </div> -->
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'LayoutNavbar',
  data: () => ({
    messages: 5,
    show: true,
    fav: true,
    menu: false,
    message: false,
    hints: true
  })
}
</script>
