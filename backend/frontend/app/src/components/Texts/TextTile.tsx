import React, { useState } from 'react'
import { Text } from './types';
import classes from './Texts.module.css';
import ExtraButton from './../UI/button/ExtraButton';

const HighlightText = ({ text, highlights }: {text:string, highlights: {start: number, end:number}[]}) => {
    let lastIndex = 0;
    const parts = [];
  
    highlights.forEach((highlight, index) => {
      const { start, end } = highlight;
      // Добавляем текст перед подчеркиваемым словом
      if (start > lastIndex) {
        parts.push(text.slice(lastIndex, start));
      }
      // Добавляем подчеркиваемое слово
      parts.push(
        <mark key={index}>
          {text.slice(start, end)}
        </mark>
      );
      lastIndex = end;
    });
  
    // Добавляем оставшийся текст
    if (lastIndex < text.length) {
      parts.push(text.slice(lastIndex));
    }
  
    return <p>{parts}</p>;
  };


function TextTile({text}: {text: Text}) {
  const sign_set = new Set([".", ",", "?"])
  const len_short_text = 200;
  const [show_all, updateShowAll] = useState(false);
  const updateShowMore = function () {
    return updateShowAll(!show_all);
  }
  const main_text = text.text.text;
  const used_words_start = new Set();
  const highlights = text.adjectives.reduce((accumulator, adj) => {
    if (!used_words_start.has(adj.key_word.start_char)) {
        used_words_start.add(adj.key_word.start_char);
        accumulator.push({start: adj.key_word.start_char, end: adj.key_word.end_char});
    }
    if (!used_words_start.has(adj.adjective.start_char)) {
        used_words_start.add(adj.adjective.start_char);
        accumulator.push({start: adj.adjective.start_char, end:adj.adjective.end_char});
    }
    return accumulator;
}, Array<{start:number, end:number}>());
highlights.sort((highlight1, highlight2) => highlight1.start - highlight2.start);
let start_short_text = Math.max(0, highlights.length > 0 ? highlights[0].start - 30: 0);
while (start_short_text < main_text.length - 1 && !sign_set.has(main_text[start_short_text++])) {
}
if (start_short_text == main_text.length) {
    start_short_text = 0
}
const sentiment = text.text.other_data.text_sentiment.label.toLowerCase();
const get_sentiment = function (sentiment) {
    switch (sentiment) {
        case "positive": 
            return "Позитивный";
        case 'negative':
            return "Негативный";
        case 'neutral':
            return "Нейтральный";
        default:
            return sentiment;
    }
}
const get_sentiment_clasname = function (sentiment) {
    switch (sentiment) {
        case "positive": 
            return classes.positive;
        case 'negative':
            return classes.negative;
        case 'neutral':
            return classes.neutral;
        default:
            return sentiment;
    }
}
const short_text =  "..." + main_text.slice(start_short_text, start_short_text + len_short_text) + "..."
  return (
    <div className={classes.card}>
        {show_all ?
        <>
            <HighlightText text={main_text} highlights={highlights} />
            <a href={text.text.link}>Источник текста {text.text.other_data.source}</a>
            <p className={classes.sentiment}>Окрас текста: <span className={get_sentiment_clasname(sentiment)}>{get_sentiment(sentiment)}</span></p>
            <p className={classes["car-info"]}>Марка: {text.text.mark}</p>
            <p className={classes["car-info"]}>Модель: {text.text.model}</p>
            <p className={classes["car-info"]}>Тип кузова: {text.text.body_type}</p>
            <ExtraButton text='less' onClick={updateShowMore} id="myBtn" />
        </>
        :
        <>
            <HighlightText text={short_text} highlights={
                highlights.filter((highlight) =>
                    highlight.start >= start_short_text && highlight.end < start_short_text + len_short_text)
                .map((highlight) => {
                    return {start: highlight.start - start_short_text + 3 , end: highlight.end - start_short_text + 3}
                })} />
            <ExtraButton text='more' onClick={updateShowMore} id="myBtn" />
        </>
        }
    </div>
  )
}

export default TextTile;