var initToggleItems = () => {
  var itemsToToggle = document.querySelectorAll(".toggle");

  // Add the button to each admonition and hook up a callback to toggle visibility
  itemsToToggle.forEach((item, index) => {
    var toggleID = `toggle-${index}`;
    item.setAttribute('id', toggleID);
    var collapseButton = `
      <button id="button-${toggleID}" class="toggle-button" data-target="${toggleID}" data-button="button-${toggleID}">
          <div class="bar horizontal" data-button="button-${toggleID}"></div>
          <div class="bar vertical" data-button="button-${toggleID}"></div>
      </button>`;
    item.insertAdjacentHTML('beforebegin', collapseButton);
    thisButton = $(`#button-${toggleID}`);
    thisButton.on('click', toggleHidden);
    if (item.classList.contains("toggle-hidden")) {
      console.log('hi')
      thisButton.addClass("toggle-button-hidden")
    }
  })
};

// This should simply add / remove the collapsed class and change the button text
var toggleHidden = (click) => {
  button = document.getElementById(click.target.dataset['button']);
  target = button.dataset['target']
  var itemToToggle = document.getElementById(target);
  if (itemToToggle.classList.contains("toggle-hidden")) {
    itemToToggle.classList.remove("toggle-hidden");
    button.classList.remove("toggle-button-hidden");
  } else {
    itemToToggle.classList.add("toggle-hidden");
    button.classList.add("toggle-button-hidden");
  }
}

// If we want to blanket-add toggle classes to certain cells
var addToggleToSelector = () => {
  const selector = "";
  document.querySelectorAll(selector).forEach((item) => {
    item.classList.add("toggle");
  })
}

// Helper function to run when the DOM is finished
const sphinxToggleRunWhenDOMLoaded = cb => {
  if (document.readyState != 'loading') {
    cb()
  } else if (document.addEventListener) {
    document.addEventListener('DOMContentLoaded', cb)
  } else {
    document.attachEvent('onreadystatechange', function() {
      if (document.readyState == 'complete') cb()
    })
  }
}
sphinxToggleRunWhenDOMLoaded(addToggleToSelector)
sphinxToggleRunWhenDOMLoaded(initToggleItems)
