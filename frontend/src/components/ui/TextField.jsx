import React from "react";
import { useIntl } from "react-intl";

export default function TextField({
  id,
  label,
  type = "text",
  value,
  placeholder,
  autoComplete,
  onChange = () => {},
}) {
  useIntl();

  return (
    <div className="flex w-full flex-col gap-2">
      <label
        htmlFor={id}
        className="text-[14px] font-medium leading-[14px] tracking-[-0.1504px] text-[#0A0A0A]"
      >
        {label}
      </label>
      <input
        id={id}
        type={type}
        value={value}
        placeholder={placeholder}
        autoComplete={autoComplete}
        onChange={(e) => onChange(e.target.value)}
        className="h-11 w-full rounded-lg border border-transparent bg-[#F3F3F5] px-3 py-1 text-[14px] tracking-[-0.1504px] text-[#0A0A0A] outline-none placeholder:text-[#717182] focus:border-[#155DFC]/30 focus:ring-2 focus:ring-[#155DFC]/15"
      />
    </div>
  );
}