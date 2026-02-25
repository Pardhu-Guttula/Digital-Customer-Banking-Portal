import React from "react";
import { useIntl } from "react-intl";

export default function CheckboxField({ id, checked, label, onChange = () => {} }) {
  const intl = useIntl();

  return (
    <div className="flex items-center gap-2">
      <input
        id={id}
        type="checkbox"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
        className="h-[13px] w-[13px] rounded-[3px] border border-[#D1D5DB] bg-white text-[#155DFC] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155DFC]/35 focus-visible:ring-offset-2 focus-visible:ring-offset-white"
      />
      <label
        htmlFor={id}
        className="text-[16px] leading-6 font-medium tracking-[-0.3125px] text-[#4A5565] select-none"
      >
        {label ?? intl.formatMessage({ id: "checkboxField.label" })}
      </label>
    </div>
  );
}