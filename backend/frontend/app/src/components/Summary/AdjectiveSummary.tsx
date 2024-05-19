import React from 'react';
import classes from './AdjectiveSummary.module.css';
import type {TextDiscription, Adjective} from './../Texts/types';

function AdjectiveSummary({texts, words, sources, marks, models, body_types}) {
  let text_data: {text:TextDiscription; adjectives:Adjective[];};
  const adjectives: Adjective[] = [];
  let text_id: string;
  for (text_id in texts) {
    text_data = texts[text_id];
    if (marks.has(text_data.text.mark) &&
        sources.has(text_data.text.other_data.source) &&
        body_types.has(text_data.text.body_type) &&
        models.has(text_data.text.model)){
            adjectives.push(...(text_data.adjectives.filter((adj: Adjective) => words.has(adj.key_word.lemma))));
        }
  }
  const accumulator: {[adj: string]: number} = {};
  const adjectives_appearance: Array<[string, number]> = Object.entries(adjectives.reduce((accumulator, adjective) => {
    const adj = adjective.adjective.lemma;
    if (!(adj in  accumulator)){
        accumulator[adj] = 0
    }
    accumulator[adj]++
    return accumulator
  }, accumulator))
  adjectives_appearance.sort(([adj1, appearance1], [adj2, appearance2]) => appearance2 - appearance1);
//   adjectives_appearance.map(function ([adjective, appearance], index) {
//      key={index} className={classes.adjective}
//         title={appearance}>{adjective}
//     
// })
  return (
    <>
        <div className={classes.box}> 
            {adjectives_appearance.map(([adj, appearance], index) => {
                return <p className={classes.adjective} key={index} title={`встречается ${appearance} раз`}> {adj}</p>
            })}
        </div>
    </>
  )
}

export default AdjectiveSummary;