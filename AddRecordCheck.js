function validateForm(z) {
  var x = document.forms["AddRecord"]["deliver_date"].value;
  var y = document.forms["AddRecord"]["quantity"].value;
  var z = document.forms["AddRecord"].submited;
  if (z == 'update') {
    if (x == null || x== "") {
      alert("請輸入數量以及日期");
      return false;
    }
    if (y == null || y== "") {
      alert("請輸入數量以及日期");
      return false;
    }
  }
}
