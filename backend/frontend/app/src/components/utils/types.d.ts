
export type  Adjective = {
  key_word: {
    word: string;
    lemma: string;
    start_char: number;
    end_char: number
  };
  adjective: {
    word: string;
    lemma: string;
    start_char: number;
    end_char: number;
    negative: boolean;
  };
}
export type  TextDiscription = {
  text: string;
  mark: string;
  model: string;
  link: string;
  body_type: string;
  other_data: {
    source: string;
    text_sentiment: {
      label: string;
      score: number;
    }
  }
};
export type  Text = {adjectives:Adjective[], text: TextDiscription, text_id: string};


export type RawData = {
      [text_id:string] :{
              text:TextDiscription;
              adjectives:Adjective[];
      };
  };