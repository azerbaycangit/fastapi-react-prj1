import { Slide } from "react-slideshow-image";
import "./assets/css/slide.css";
import { useEffect, useState } from "react";
import axios from "axios";

const properties = {
  duration: 5000,
  transitionDuration: 500,
  infinite: true,
  indicators: true,
  arrows: true,
};

const App = () => {
  const [obj, setObj] = useState();
  useEffect(() => {
    axios.get("http://localhost:8000").then((e) => setObj(e?.data));
  }, []);
  console.log(obj);
  return (
    <Slide {...properties}>
      {obj?.data?.map((item) => (
        <div className="each-slide" key={item.title}>
          <div style={{ backgroundImage: `url(${item.url})` }}>
            <span style={{ fontSize: 50, color: "white" }}>{item.title}</span>
          </div>
        </div>
      ))}
    </Slide>
  );
};

export default App;
