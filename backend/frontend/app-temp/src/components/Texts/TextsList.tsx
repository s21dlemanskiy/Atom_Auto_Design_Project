import React from 'react';
import TextTile from './TextTile';
import type {Adjective, Text, RawData, TextDiscription} from './types';
// import type {Text} from './types';
// import type {TextDiscription} from './types';

type InputType = {
    texts:RawData;
    words: Set<string>;
    sources: Set<string>;
    marks: Set<string>;
    models: Set<string>;
    body_types: Set<string>;
}

function TextsList({texts, words, sources, marks, models, body_types}:InputType) {
  const texts_list: Text[] = [];
  let text_data: {text:TextDiscription; adjectives:Adjective[];};
  let adjectives: Adjective[];
  let text_id: string;
  for (text_id in texts) {
    text_data = texts[text_id];
    if (marks.has(text_data.text.mark) &&
        sources.has(text_data.text.other_data.source) &&
        body_types.has(text_data.text.body_type) &&
        models.has(text_data.text.model)){
            adjectives = text_data.adjectives.filter((adj: Adjective) => words.has(adj.key_word.lemma));
            if (adjectives.length > 0){
                texts_list.push({adjectives:adjectives, text: text_data.text, text_id: text_id})
                }
        }
  }
  return (
    <div>
        {texts_list.map((text: Text) =>
            <div key={text.text_id}>
                <TextTile text={text} />
            </div>
        )}
    </div>
  )
}

export default TextsList;