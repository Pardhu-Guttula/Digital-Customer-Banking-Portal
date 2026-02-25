import React from "react";
import { useIntl } from "react-intl";

export default function LabeledInput({
  id,
  label,
  type = "text",
  value,
  placeholder,
  onChange = () => {},
  autoComplete,
}) {
  const intl = useIntl();

  return (
    <div className="flex flex-col gap-2">
      <label htmlFor={id} className="text-sm font-medium leading-none text-[#0A0A0A]">
        {label}
      </label>
      <input
        id={id}
        type={type}
        value={value}
        placeholder={placeholder}
        autoComplete={autoComplete}
        onChange={(e) => onChange(e.target.value)}
        className="h-11 w-full rounded-lg border border-transparent bg-[#F3F3F5] px-3 text-sm text-[#0A0A0A] outline-none placeholder:text-[#717182] focus:border-[#CBD5E1] focus:bg-white"
        aria-label={intl.formatMessage({ id: "labeledInput.ariaLabel" })}
      />
    </div>
  );
}