import React from "react";
import { useIntl } from "react-intl";

export default function LabeledInput({
  id,
  label,
  type = "text",
  value,
  onChange = () => {},
  placeholder = "",
  autoComplete,
}) {
  const intl = useIntl();

  return (
    <div className="flex flex-col gap-2 w-full">
      <label
        htmlFor={id}
        className="text-[14px] leading-[14px] font-medium tracking-[-0.1504px] text-[#0a0a0a]"
      >
        {label}
      </label>

      <input
        id={id}
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        autoComplete={autoComplete}
        className="h-11 w-full rounded-lg bg-[#f3f3f5] px-3 py-1 text-[14px] tracking-[-0.1504px] text-[#111827] placeholder:text-[#717182] outline-none ring-0 border border-transparent focus:border-[#155dfc]/30 focus:ring-4 focus:ring-[#155dfc]/10"
      />
    </div>
  );
}