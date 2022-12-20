import axios from "axios";
const server = `http://localhost:8000`;

export const getNaverMovie = (req) =>
  axios.get(`${server}/webcrawler/naver?req=${req}`);
