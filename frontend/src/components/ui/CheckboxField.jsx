import React, { useId } from "react";
import { useIntl } from "react-intl";

export default function CheckboxField({ checked, label, onChange = () => {} }) {
  useIntl();
  const id = useId();

  return (
    <div className="flex items-center gap-2">
      <input
        id={id}
        type="checkbox"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
        className="h-[13px] w-[13px] rounded border border-[#D0D5DD] bg-white align-middle accent-[#155DFC] focus:outline-none focus:ring-2 focus:ring-[#155DFC]/20"
      />
      <label
        htmlFor={id}
        className="text-base font-medium leading-6 tracking-[-0.3125px] text-[#4A5565] select-none"
      >
        {label}
      </label>
    </div>
  );
}