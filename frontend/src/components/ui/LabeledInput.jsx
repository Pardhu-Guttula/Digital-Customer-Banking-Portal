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
  inputMode,
}) {
  const intl = useIntl();

  return (
    <div className="flex flex-col gap-2 w-full">
      <label
        htmlFor={id}
        className="text-[14px] leading-[14px] font-medium tracking-[-0.1504px] text-[#0A0A0A]"
      >
        {label ?? intl.formatMessage({ id: "labeledInput.label" })}
      </label>

      <input
        id={id}
        type={type}
        value={value}
        placeholder={placeholder ?? intl.formatMessage({ id: "labeledInput.placeholder" })}
        onChange={(e) => onChange(e.target.value)}
        autoComplete={autoComplete}
        inputMode={inputMode}
        className="h-11 w-full rounded-lg bg-[#F3F3F5] px-3 py-1 text-[14px] tracking-[-0.1504px] text-[#0A0A0A] placeholder:text-[#717182] outline-none ring-1 ring-transparent focus:ring-[#155DFC]/35"
      />
    </div>
  );
}