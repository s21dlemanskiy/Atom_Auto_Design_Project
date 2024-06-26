import React, { ChangeEvent, useState, useEffect, useRef } from 'react';
import classes from './MultiplySelection.module.css';

type OptionValue = string;
type InputType = {
    func: (selected_values: Set<OptionValue>) => void;
    options: Set<OptionValue>;
    selected_options: Set<OptionValue>;
    updateSelected: (Set<OptionValue>);
    name_map: {[value:OptionValue]: string}
}

function MultiplySelection({func, options, selected_options, updateSelected, name_map, ...props}: InputType) {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const containerRef = useRef(null);
  const isSelected = (opt_value: OptionValue) => selected_options.has(opt_value);
  const changeOption = (opt_value: OptionValue, selected: boolean) => {selected ? 
    selected_options.add(opt_value) && updateSelected(new Set(selected_options)):
    selected_options.delete(opt_value) && updateSelected(new Set(selected_options))}
  const onCheckBoxChange = (e: ChangeEvent<HTMLInputElement>) => {
    changeOption(e.target.value, e.target.checked);
    func(selected_options);
  }
  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };
  const hideDropdown = (event) => {
    console.log(containerRef.current.contains(event.target), event.relatedTarget)
    if (containerRef.current && !containerRef.current.contains(event.relatedTarget)) {
      setDropdownOpen(false);
    }
  }
  const showDropdown = () => {
    setDropdownOpen(true);
  }
  useEffect(() => {
    const container = containerRef.current;

    if (container) {
      container.addEventListener('focusin', showDropdown);
      container.addEventListener('focusout', hideDropdown);

      return () => {
        container.removeEventListener('focusin', showDropdown);
        container.removeEventListener('focusout', hideDropdown);
      };
    }
  }, []);
  return (
    <div {...props} className={classes.dropdown} ref={containerRef} tabIndex="-1">
        <button className={classes.dropbtn}>
        {[...options].reduceRight((values:string[], option:OptionValue) =>  selected_options.has(option) ?
              [option in name_map ? name_map[option]: option, ...values]:
              [...values], []).join(", ")}</button>
        {dropdownOpen && (
            <div className={classes.dropdownContent}>
                {[...options].map((option: OptionValue) => 
                    <label key={option}><input type="checkbox" defaultChecked={isSelected(option)} onChange={onCheckBoxChange} name={option in name_map ? name_map[option]: option.toString()} value={option} />{option in name_map ? name_map[option]: option.toString()}</label>
                )}
            </div>
        )}
    </div>
  )
}

export default MultiplySelection