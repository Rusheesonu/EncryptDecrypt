<template>
  <v-navigation-drawer id="appDrawer" :mini-variant.sync="mini" fixed :dark="$vuetify.dark" app v-model="drawer"
    permanent expand-on-hover>
    <v-toolbar color="primary darken-1" dark>
      <img src="../static/m.png" height="36" alt="Vue Material Admin Template">
      <v-toolbar-title class="ml-0 pl-3">
        <span class="hidden-sm-and-down">CryptoE</span>
      </v-toolbar-title>
    </v-toolbar>
    <vue-perfect-scrollbar class="drawer-menu--scroll" :settings="scrollSettings">
      <v-list dense expand>
        <template v-for="(item, i) in menus">
          <!--group with subitems-->
          <v-list-group v-if="item.items" :key="item.name" :group="item.group" :prepend-icon="item.icon"
            no-action="no-action">
            <v-list-tile slot="activator" ripple="ripple">
              <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <template v-for="(subItem, i) in item.items">
              <!--sub group-->
              <v-list-group v-if="subItem.items" :key="subItem.name" :group="subItem.group" sub-group="sub-group">
                <v-list-tile slot="activator" ripple="ripple">
                  <v-list-tile-content>
                    <v-list-tile-title>{{ subItem.title }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile v-for="(grand, i) in subItem.children" :key="i" :to="grand.href? grand.href : null"
                  ripple="ripple">
                  <v-list-tile-content>
                    <v-list-tile-title>{{ grand.title }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list-group>
              <!--child item-->
              <v-list-tile v-else :key="i" :to="subItem.href? subItem.href : null" :disabled="subItem.disabled"
                :target="subItem.target" ripple="ripple">
                <v-list-tile-content>
                  <v-list-tile-title><span>{{ subItem.title }}</span></v-list-tile-title>
                </v-list-tile-content>
                <v-list-tile-action v-if="subItem.action">
                  <v-icon :class="[subItem.actionClass || 'success--text']">{{ subItem.action }}</v-icon>
                </v-list-tile-action>
              </v-list-tile>
            </template>
          </v-list-group>
          <v-subheader v-else-if="item.header" :key="i">{{ item.header }}</v-subheader>
          <v-divider v-else-if="item.divider" :key="i"></v-divider>
          <!--top-level link-->
          <v-list-tile v-else :to="item.href ? item.href : null" ripple="ripple" :disabled="item.disabled"
            :target="item.target" rel="noopener" :key="item.name">
            <v-list-tile-action v-if="item.icon">
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile-content>
            <v-list-tile-action v-if="item.subAction">
              <v-icon class="success--text">{{ item.subAction }}</v-icon>
            </v-list-tile-action>
          </v-list-tile>
        </template>
      </v-list>
    </vue-perfect-scrollbar>
  </v-navigation-drawer>
</template>
<script>
import menu from '@/api/menu';
import VuePerfectScrollbar from 'vue-perfect-scrollbar';

export default {
  name: 'app-drawer',
  components: {
    VuePerfectScrollbar,
  },
  props: {
    expanded: {
      type: Boolean,
      default: true
    },
  },
  data: () => ({
    mini: false,
    menus: menu,
    scrollSettings: {
      maxScrollbarLength: 160
    }
  }),
  computed: {
    drawer: {
      get() {
        return this.$store.state.drawer
      },
      set(val) {
        this.$store.commit('drawer', val)
      }
    },
    computeGroupActive() {
      return true;
    },
    sideToolbarColor() {
      return this.$vuetify.options.extra.sideNav;
    }
  },
  methods: {
    genChildTarget(item, subItem) {
      if (subItem.href) return;
      if (subItem.component) {
        return {
          name: subItem.component,
        };
      }
      return { name: `${item.group}/${(subItem.name)}` };
    },
  }
};
</script>


<style lang="stylus">
  #appDrawer
    overflow: hidden
    .drawer-menu--scroll
      height: calc(100vh - 48px)
      overflow: auto

</style>
