/*
 * -< FORM ANIMATION >-
 */

var formElement = "";
var displayWidth;
var elementWidth;

function getElementWidth()  {
    return document.getElementById('form_password_first').offsetWidth;
}

function getWidth() {
  if (self.innerWidth) {
    return self.innerWidth;
  }

  if (document.documentElement && document.documentElement.clientWidth) {
    return document.documentElement.clientWidth;
  }

  if (document.body) {
    return document.body.clientWidth;
  }
}

elementWidth = getElementWidth();
display_Width = getWidth();
display_point = display_point - elementWidth - 20;

function moveFormInputElement()  {
    formElement.style.left = parseInt(formElement.style.left)-200+'px';
    setTimeout(moveFormInputElement, 10);
}

function initMoveFormInputElement() {
    formElement = document.getElementById('form_password_first'); // get the "foo" object
    formElement.style.left = display_point_fixed + 'px'; // set its initial position to 0px
    moveFormInputElement(); // start animating
}
window.alert(display_point)
window.onload = initMoveFormInputElement;

/* -< FA >- */