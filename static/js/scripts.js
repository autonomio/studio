  function tightRows() {
    var element = document.getElementById("data_frame");
    element.classList.toggle("display_tight");
}


   $(document).ready(function () {
       $('#sidebarCollapse').on('click', function () {
           $('#sidebar').toggleClass('active');
       });
   });
