const addBoxButton = document.querySelector('[data-add-box]');
const grid = document.querySelector('.grid');
const boxes = document.querySelectorAll('.box');

addBoxButton.addEventListener('click', () => {
  const box = document.createElement('div');
  box.classList.add('box');
  grid.append(box);
});

function addGlobalEventListener(type, selector, callback, parent = document){
  parent.addEventListener(type, e => {
    if (e.target.matches(selector)){
      callback(e)
    }
  })
}

addGlobalEventListener('click', '.box', e => { e.target.classList.toggle('clicked')}, grid)


// document.addEventListener('click', e => {
//   if (e.target.matches('.box')){
//     e.target.classList.toggle('clicked')
//   }
// })


// Event Listeners

const grandparent = document.querySelector('.grandparent');
const parent = document.querySelector('.parent');
const child = document.querySelector('.child');


grandparent.addEventListener('click', e => {console.log('Grandparent 1')});
parent.addEventListener('click', e => {console.log('Parent 1')});
child.addEventListener('click', e => {console.log('Child 1')});
document.addEventListener('click', e => {
  console.log('Document 1')});