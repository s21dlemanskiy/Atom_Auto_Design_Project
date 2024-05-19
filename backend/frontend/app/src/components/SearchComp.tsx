import React from 'react'
import { useState, useEffect } from 'react'
import MyButton from './UI/button/MyButton';
import ExtraButton from './UI/button/ExtraButton';
import MultiplySelection from './UI/multiselect/MultiplySelection';
import TextsList from './Texts/TextsList';
import getFilters from './utils/getFiltersFromTexts';
import { RawData } from './Texts/types';
import classes from './SearchComp.module.css';
import AdjectiveSummary from './Summary/AdjectiveSummary';

function SearchComp({texts}) {
    const [available_words, available_sources, available_marks, available_models, available_body_types] = getFilters(texts);
    const [words, setWords] = useState(new Set([...available_words]));
    const [sources, setSources] = useState(new Set([...available_sources]));
    const [marks, setMarks] = useState(new Set([...available_marks]));
    const [models, setModels] = useState(new Set([...available_models]));
    const [body_types, setBodyTypes] = useState(new Set([...available_body_types]));
    // const updateFilters = function (texts:RawData) {
    //     const {words, sources, marks, models, body_types} = getFilters(texts);
    //     setWords(words);
    //     setSources(sources);
    //     setMarks(marks);
    //     setBodyTypes(body_types);
    //     setModels(models)
    //   }
    useEffect(() => {
        setWords(new Set([...available_words]));
        setSources(new Set([...available_sources]));
        setMarks(new Set([...available_marks]));
        setBodyTypes(new Set([...available_body_types]));
        setModels(new Set([...available_models]))
      }, [texts]);
    // setWords(new Set([...available_words]));
    return (
      <>
        { 0 < Math.min(available_words.size, available_sources.size, available_marks.size, available_models.size, available_body_types.size) ?
        <div>
            <div id='TextFitlers' className={classes["dropdown-list"]}>
                <div className={classes["dropdown-item"]}>
                    <h3>Выбор синонимов</h3>
                    <div className={classes["dropdown"]}>
                        <MultiplySelection id="wordsFilter" func={(e) => console.log(e)} options={available_words} selected_options={words} updateSelected={setWords} name_map={{}}/>
                    </div>
                </div>
                <div className={classes["dropdown-item"]}>
                    <h3>Выбор источника</h3>
                    <div className={classes["dropdown"]}>
                    <MultiplySelection func={(e) => console.log(e)} options={available_sources} selected_options={sources} updateSelected={setSources} name_map={{}} />
                    </div>
                </div>
                <div className={classes["dropdown-item"]}>
                    <h3>Выбор марок</h3>
                    <div className={classes["dropdown"]}>
                        <MultiplySelection func={(e) => console.log(e)} options={available_marks} selected_options={marks} updateSelected={setMarks} name_map={{}} />
                    </div>
                </div>
                <div className={classes["dropdown-item"]}>
                    <h3>Выбор моделей</h3>
                    <div className={classes["dropdown"]}>
                        <MultiplySelection func={(e) => console.log(e)} options={available_models} selected_options={models} updateSelected={setModels} name_map={{}} />
                    </div>
                </div>
                <div className={classes["dropdown-item"]}>
                    <h3>Выбор типа корпуса</h3>
                    <div className={classes["dropdown"]}>
                    <MultiplySelection func={(e) => console.log(e)} options={available_body_types} selected_options={body_types} updateSelected={setBodyTypes} name_map={{}} />
                    </div>
                </div>
            </div>
            <div id="AdjectiveSummary">
                <AdjectiveSummary texts={texts} words={words} sources={sources} marks={marks} models={models} body_types={body_types} />
            </div>
            <div id="TextList">
                <TextsList texts={texts} words={words} sources={sources} marks={marks} models={models} body_types={body_types} />
            </div>
        </div>
        :
        <h2>No data found</h2>
        }
      </>
    )
}

export default SearchComp