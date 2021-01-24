$('#delete-film-modal').on('show.bs.modal', function (event) {
    let url = event.relatedTarget.dataset.url;
    let form = this.querySelector('form');
    form.action = url;
    let filmName = event.relatedTarget.closest('tr').querySelector('.film-title').textContent;
    this.querySelector('#film-title').textContent = filmName;
})