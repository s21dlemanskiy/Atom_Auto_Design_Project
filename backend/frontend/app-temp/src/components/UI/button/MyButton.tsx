import React, { MouseEventHandler } from 'react';
import classes from './MyButton.module.css';
type InputType = {
    text: string;
    func: MouseEventHandler<HTMLButtonElement>;
}

function MyButton({text, func, ...props}:InputType) {
  return (
    <button {...props} onClick={func} className={classes.searchButton}>{text}</button>
  )
}

export default MyButton