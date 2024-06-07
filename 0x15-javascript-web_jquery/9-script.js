$("document").ready(function () {
  $.get("https://fourtonfish.com/hellosalut/?lang=fr", function (result) {
    $("DIV#hello").text(result.hello);
  });
});
