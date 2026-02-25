import React from "react";
import { useIntl } from "react-intl";
import cx from "../utils/cx";

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
        className="text-[14px] leading-[14px] font-medium text-[#0a0a0a] tracking-[-0.1504px]"
      >
        {label}
      </label>
      <input
        id={id}
        type={type}
        value={value}
        placeholder={placeholder}
        autoComplete={autoComplete}
        inputMode={inputMode}
        onChange={(e) => onChange(e.target.value)}
        className={cx(
          "h-11 w-full rounded-lg bg-[#f3f3f5] px-3 py-1 text-[14px] tracking-[-0.1504px]",
          "text-[#0a0a0a] placeholder:text-[#717182]",
          "border border-transparent focus:border-[#155dfc]/30 focus:ring-2 focus:ring-[#155dfc]/20 outline-none"
        )}
        aria-label={intl.formatMessage({ id: "labeledInput.ariaLabel" })}
      />
    </div>
  );
}