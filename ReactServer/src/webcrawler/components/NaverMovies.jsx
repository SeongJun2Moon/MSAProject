import { getNaverMovie } from "webcrawler/api";

const NaverMovie = () => {
  const onClick = (e) => {
    e.preventDefault();
    alert(`됨`);
    getNaverMovie().then((response) => {
      console.log(`response is ${response.data.result}`);
      localStorage.setItem("token", JSON.stringify(response.data.result));
      alert(`정보 : ${JSON.stringify(response.data.result)}`);
    });
  };

  return (
    <>
      <h2>네이버 크롤러</h2>
      <button onClick={onClick}>네이버 영화 크롤링</button>
      <p>버튼을 클릭하시면, 네이버 영화 목록이 출력됩니다.</p>
    </>
  );
};
export default NaverMovie;
