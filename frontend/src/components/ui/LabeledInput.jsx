import React from "react";
import { useIntl } from "react-intl";

function noop() {}

export default function LabeledInput({
  id,
  label,
  type = "text",
  value,
  placeholder,
  onChange = noop,
  autoComplete,
}) {
  const intl = useIntl();

  const resolvedLabel = label ?? intl.formatMessage({ id: "labeledInput.label" });
  const resolvedPlaceholder = placeholder ?? intl.formatMessage({ id: "labeledInput.placeholder" });

  return (
    <div className="flex w-full flex-col gap-2">
      <label
        htmlFor={id}
        className="text-[14px] font-medium leading-[14px] tracking-[-0.1504px] text-[#0A0A0A]"
      >
        {resolvedLabel}
      </label>
      <input
        id={id}
        type={type}
        value={value}
        placeholder={resolvedPlaceholder}
        autoComplete={autoComplete}
        onChange={(e) => onChange(e.target.value)}
        className="h-11 w-full rounded-lg border border-transparent bg-[#F3F3F5] px-3 py-1 text-[14px] tracking-[-0.1504px] text-[#111827] placeholder:text-[#717182] focus:outline-none focus:ring-2 focus:ring-[#155DFC]/30"
      />
    </div>
  );
}