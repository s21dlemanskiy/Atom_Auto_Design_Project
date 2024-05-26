import React, { FC }from 'react';
import classes from './ExtraButton.module.css';

type InputType = { text: string; }
type InputTypeWithProps = InputType & React.HTMLAttributes<HTMLButtonElement>;

// function ExtraButton ({text, ...props}) {
//   return (
//     <button {...props} className={classes.extraButton}>{text}</button>
//   )
// }

const ExtraButton: FC<InputTypeWithProps> = function ExtraButton ({text, ...props}) {
  return (
    <button {...props} className={classes.extraButton}>{text}</button>
  )
}

export default ExtraButton