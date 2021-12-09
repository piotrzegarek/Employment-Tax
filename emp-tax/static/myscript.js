var topnav = document.getElementById('topbar')
var sidenav = document.getElementById('msb')



$('.form-control').change(function() {
    selectedItem = $('.form-control').val();
    if (selectedItem == "1") {
        topnav.classList.remove("dark-theme")
        sidenav.classList.remove("dark-theme")
        topnav.classList.add("light-theme")
        sidenav.classList.add("light-theme")
    } else {
        topnav.classList.remove("light-theme")
        sidenav.classList.remove("light-theme")
        topnav.classList.add("dark-theme")
        sidenav.classList.add("dark-theme")
    }
});