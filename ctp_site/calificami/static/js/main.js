window.onload = function () {
    const menu_btn = document.querySelector('.hamburger');
    const mobile_menu = document.querySelector('.mobile-nav');

    menu_btn.addEventListener('click', function () { 
        menu_btn.classList.toggle('is-active');
        mobile_menu.classList.toggle('is-active');
    });
}


async function waitForMs(ms) {
    await new Promise(resolve => setTimeout(resolve, ms));
  }
  
  async function typeSentence(sentence, target) {
    const letters = sentence.split('');
    for (const letter of letters) {
      await waitForMs(100);
      document.querySelector(target).innerHTML += letter;
    }
  }
  
  async function deleteSentence(target) {
    const sentence = document.querySelector(target).innerHTML;
    const letters = sentence.split('');
  
    while (letters.length > 0) {
      await waitForMs(100);
      letters.pop();
      document.querySelector(target).innerHTML = letters.join('');
    }
  }
  
  const words = [
    "Hello,",
    "Welcome,",
    "Typing Effect"
  ];
  
  let wordIndex = 0;
  
  async function showNextWord() {
    const featureText = document.querySelector('.feature-text');
    featureText.style.color = getRandomColor();
    await typeSentence(words[wordIndex], '#feature-text');
    await waitForMs(2000);
    deleteSentence('#feature-text');
    wordIndex = (wordIndex + 1) % words.length;
    showNextWord();
  }
  
  function getRandomColor() {
    const colors = ['#FF5733', '#33FF61', '#33A9FF', '#B733FF'];
    return colors[Math.floor(Math.random() * colors.length)];
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    showNextWord();
  });
  
  
  