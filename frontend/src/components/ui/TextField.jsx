import React from "react";
import { useIntl } from "react-intl";

function noop() {}

export default function TextField({
  id,
  label,
  type = "text",
  name,
  value,
  onChange = noop,
  placeholder,
  autoComplete,
}) {
  const intl = useIntl();

  const resolvedLabel = label ?? intl.formatMessage({ id: "textField.label" });
  const resolvedPlaceholder =
    placeholder ?? intl.formatMessage({ id: "textField.placeholder" });

  return (
    <div className="flex w-full flex-col gap-2">
      <label
        htmlFor={id}
        className="text-sm font-medium leading-[14px] tracking-[-0.1504px] text-[#0a0a0a]"
      >
        {resolvedLabel}
      </label>

      <input
        id={id}
        name={name}
        type={type}
        value={value}
        placeholder={resolvedPlaceholder}
        autoComplete={autoComplete}
        onChange={(e) => onChange(e.target.value)}
        className="h-11 w-full rounded-lg border border-transparent bg-[#f3f3f5] px-3 py-1 text-sm tracking-[-0.1504px] text-[#0a0a0a] outline-none transition focus:border-[#155dfc]/30 focus:ring-2 focus:ring-[#155dfc]/20"
      />
    </div>
  );
}