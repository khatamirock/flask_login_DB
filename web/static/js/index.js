

note_card = document.querySelectorAll('.notes-card');
delbtn = document.querySelectorAll('.delbtn');







// pop up starts here
const noteCard = document.querySelectorAll('.notes-card');
const popcard = document.querySelector('.popup-card .doc');
const noteParent = document.querySelector('.card-container');
const closeBtn = document.querySelector('.close');




if (noteParent) {
    noteParent.addEventListener('click', function (e) {
        const target = e.target.closest('.notes-card');
        if (!target) {
            popcard.classList.add('hide');
            return;
        }
        const text = target.querySelector('.note-body b').innerHTML;
        popcard.querySelector('b').innerHTML = text;
        popcard.classList.toggle('hide');

    });
    closeBtn.addEventListener('click', function () {
        popcard.classList.add('hide');
    });
}


// pop up ends here







