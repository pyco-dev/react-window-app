import { useState, useEffect } from "react";

export default function App() {
  const [number, setNumber] = useState(1);

  useEffect(() => {
    setTimeout(() => {
      setNumber(number + 1);
    }, 1000);
  }, [number]);

  return <h1>working! number state = {number}</h1>;
}
