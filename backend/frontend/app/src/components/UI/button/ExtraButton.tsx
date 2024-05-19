import React, { MouseEventHandler } from 'react';
import classes from './ExtraButton.module.css';

type InputType = {
    text: string;
    func: MouseEventHandler<HTMLButtonElement>;
}

function ExtraButton({text, ...props}:InputType) {
  return (
    <button {...props} className={classes.extraButton}>{text}</button>
  )
}

export default ExtraButton