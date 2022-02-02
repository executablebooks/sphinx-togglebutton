/**
 * Add Toggle Buttons to elements
 */

let doc_url_root = DOCUMENTATION_OPTIONS.URL_ROOT;
if (doc_url_root == '#') {
    doc_url_root = '';
}

const path_static = `${doc_url_root}_static/`;

var initToggleItems = () => {
  var itemsToToggle = document.querySelectorAll(togglebuttonSelector);
  console.log(`[togglebutton]: Adding toggle buttons to ${itemsToToggle.length} items`)
  // Add the button to each admonition and hook up a callback to toggle visibility
  itemsToToggle.forEach((item, index) => {
    // Generate unique IDs for this item
    var toggleID = `toggle-${index}`;
    var buttonID = `button-${toggleID}`;

    item.setAttribute('id', toggleID);
    if (!item.classList.contains("toggle")){
      item.classList.add("toggle");
    }

    // This is the button that will be added to each item to trigger the toggle
    var collapseButton = `
      <button type="button" id="${buttonID}" class="toggle-button" data-target="${toggleID}" data-button="${buttonID}">
          <img class="tb-icon" src="${path_static}togglebutton-chevron.svg">
      </button>`;

    // Add the button HTML to this element and assign it as a variable to use later
    if (item.classList.contains("admonition")) {
      // If it's an admonition block, then we'll add the button inside
      item.insertAdjacentHTML("afterbegin", collapseButton);
    } else {
      item.insertAdjacentHTML('beforebegin', collapseButton);
    }
    thisButton = document.getElementById(buttonID);
    
    // Add click handlers for the button + admonition title (if admonition)
    thisButton.addEventListener('click', toggleClickHandler);

    // If admonition has a single direct-child title make it clickable.
    admonitionTitle = document.querySelector(`#${toggleID} > .admonition-title`)
    if (admonitionTitle) {
      admonitionTitle.addEventListener('click', toggleClickHandler);
      admonitionTitle.dataset.target = toggleID
      admonitionTitle.dataset.button = buttonID
    }

    // Now hide the item for this toggle button unless explicitly noted to show
    if (!item.classList.contains("toggle-shown")) {
      toggleHidden(thisButton);
    }
  })
};

// This should simply add / remove the collapsed class and change the button text
var toggleHidden = (button) => {
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

var toggleClickHandler = (click) => {
  if (click.target.tagName == "IMG") {
    parent = click.target.parentElement;
  } else {
    parent = click.target;
  }
  button = document.getElementById(parent.dataset['button']);
  toggleHidden(button);
}

// If we want to blanket-add toggle classes to certain cells
var addToggleToSelector = () => {
  const selector = "";
  if (selector.length > 0) {
    document.querySelectorAll(selector).forEach((item) => {
      item.classList.add("toggle");
    })
  }
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
