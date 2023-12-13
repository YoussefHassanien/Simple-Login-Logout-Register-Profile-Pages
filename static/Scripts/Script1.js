const selectImage = document.querySelector('.contact .roww .btn5');
const inputFile = document.querySelector('#file');
const imgArea = document.querySelector('.contact .roww form .co .imga');

selectImage.addEventListener('click', function () {
    inputFile.click();
})

inputFile.addEventListener('change', function () {
    const image = this.files[0]
    console.log(image);
    const reader = new FileReader();
    reader.onload = () => {
        const imgUrl = reader.result;
        const img = document.createElement('img')
        img.src = imgUrl;
        imgArea.innerHTML = ''; // Clear previous images
        imgArea.appendChild(img);
        imgArea.classList.add('active');
        imgArea.dataset.img = image.name;
    }
    reader.readAsDataURL(image);
})
