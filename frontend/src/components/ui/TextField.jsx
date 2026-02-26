import React from "react";

export default function TextField({
  id,
  label,
  type = "text",
  value,
  placeholder,
  onChange = () => {},
  autoComplete,
  styles,
}) {
  return (
    <div style={styles.field}>
      <label htmlFor={id} style={styles.label}>
        {label}
      </label>
      <input
        id={id}
        type={type}
        value={value}
        placeholder={placeholder}
        autoComplete={autoComplete}
        onChange={(e) => onChange(e.target.value)}
        style={styles.input}
      />
    </div>
  );
}