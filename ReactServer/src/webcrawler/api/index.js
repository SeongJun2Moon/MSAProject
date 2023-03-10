// import axios from "axios";
// const server = `http://localhost:8000`;

// export const getNaverMovie = (req) =>
//   axios.get(`${server}/webcrawler/naver?req=${req}`);
const webcrawler = `/webcrawler/naver`
const server = "http://127.0.0.1:8000/"

const webcrawlerService = {
    naverMovie
}

const handleResponse = (response) => { 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
}

async function naverMovie(){
    const res = await fetch(`${server}${webcrawler}`)
    .then(handleResponse)
    .then(data => JSON.stringify(data)) //JSON.stringify() : 딕셔너리를 JSON으로 변환 
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
}
export default webcrawlerService