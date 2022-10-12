const Menu = [
  {header: 'Apps'},
  {
    title: 'Sign',
    icon: ' fa-regular fa-lock',
    name: 'Sign',
    href: '/sign'
  },
  {
    title: 'Verify',
    icon: 'fa-regular fa-lock',
    name: 'Sign',
    href: '/verify'
  },
  {
    title: 'Encrypt',
    icon: 'dashboard',
    name: 'Sign',
    href: '/encrypt'
  },
  {
    title: 'Decrypt',
    icon: 'dashboard',
    name: 'Sign',
    href: '/decrypt'
  },
];
// reorder menu
Menu.forEach((item) => {
  if (item.items) {
    item.items.sort((x, y) => {
      let textA = x.title.toUpperCase();
      let textB = y.title.toUpperCase();
      return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
    });
  }
});

export default Menu;
