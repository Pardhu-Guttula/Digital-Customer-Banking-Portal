import React from "react";
import { useIntl } from "react-intl";
import cn from "../utils/cx";

function noop() {}

export default function LabeledInput({
  id,
  label,
  type = "text",
  value,
  placeholder,
  onChange = noop,
  autoComplete,
  inputMode,
  name,
}) {
  useIntl(); // present per i18n rule; label/placeholder are passed in already formatted

  return (
    <div className="flex w-full flex-col gap-2">
      <label
        htmlFor={id}
        className="text-[14px] font-medium leading-[14px] tracking-[-0.1504px] text-[#0a0a0a]"
      >
        {label}
      </label>

      <input
        id={id}
        name={name}
        type={type}
        value={value}
        placeholder={placeholder}
        onChange={(e) => onChange(e.target.value)}
        autoComplete={autoComplete}
        inputMode={inputMode}
        className={cn(
          "h-11 w-full rounded-lg border border-transparent bg-[#f3f3f5] px-3 py-1 text-[14px] tracking-[-0.1504px] text-[#0a0a0a] outline-none",
          "placeholder:text-[#717182]",
          "focus:border-[#155dfc]/30 focus:ring-2 focus:ring-[#155dfc]/20"
        )}
      />
    </div>
  );
}