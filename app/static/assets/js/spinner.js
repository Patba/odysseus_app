const loaderContainer = document.querySelector('.container-loader')
const getSendTicket = document.querySelector('.send-ticket')

const displayLoading = () => {
    loaderContainer.style.display = 'flex';
};

const hideLoading = () => {
    loaderContainer.style.display = 'none';
};

getSendTicket.addEventListener('click', () => {
    displayLoading()
})



