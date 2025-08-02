export function getCats() {
    return fetch('http://localhost:8000/api/cats/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })        
}