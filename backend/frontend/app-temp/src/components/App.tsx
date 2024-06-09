import React from 'react';
import { useState } from 'react';
// import { RawData } from './Texts/types';
import SearchComp from './SearchComp';
import MyButton from './UI/button/MyButton';
// import ExtraButton from './UI/button/ExtraButton';
import axios from 'axios';
import { RawData } from './Texts/types';

const host = window.location.hostname;
const protocol = window.location.protocol;
const port = "80";
function App() {
  // let data_example: RawData = {};
  const defaultSearchWord = "машина";
  const [searchWord, setSearchWord] = useState(defaultSearchWord);
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const [texts, setTexts] = useState({} as RawData);
  const updateWordValue = (evt: { target: { value: React.SetStateAction<string>; }; }) => setSearchWord(evt.target.value);
  // fetch('./DataExample.json')
  //   .then((response) => response.json()).then((json) => {data_example = json});, 
      // { params: { word: searchWord.toString() } 
  const updateTexts = function () {axios.get(`${protocol}//${host}:${port}/api/search/synonims`, { params: { word: searchWord.toString() } }
).then(function (response) {
        console.log(response.data);
        axios.post(`${protocol}//${host}:${port}/api/search/`, response.data).then(function (response) {
            setTexts(response.data);
            if (Object.keys(response.data).length == 0) {
              alert("Ничего не найдено");
            }
          })
          .catch(function (error) {
            console.log("response2");
            alert("ошбка связи с бекедом");
            console.log(error);
          })
      })
      .catch(function (error) {
        console.log("response1");
        alert("ошбка связи с бекедом");
        console.log(error);
      });
    }

  return (
    <>
      <input placeholder={searchWord} type="text" onChange={updateWordValue}></input>
      <MyButton text='update keyword' func={updateTexts} />
      <SearchComp texts={texts} />
    </>
  )
}

export default App
