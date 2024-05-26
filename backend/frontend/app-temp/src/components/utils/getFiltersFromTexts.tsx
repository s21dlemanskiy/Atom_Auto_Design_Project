
import type { RawData } from "./types";
const getFilters = function (text: RawData){
    const words = new Set<string>();
    const sources = new Set<string>();
    const marks = new Set<string>();
    const models = new Set<string>();
    const body_types = new Set<string>();
    // eslint-disable-next-line prefer-const
    for (let text_id in text){
        text[text_id].adjectives.forEach((adj: {key_word: {lemma: string}}) => words.add(adj.key_word.lemma))
        body_types.add(text[text_id].text.body_type)
        sources.add(text[text_id].text.other_data.source)
        marks.add(text[text_id].text.mark)
        models.add(text[text_id].text.model)
    }
    return [words, sources, marks, models, body_types]
}
export default getFilters;