import React, { useId } from "react";
import { useIntl } from "react-intl";

function noop() {}

export default function CheckboxField({ checked, label, onChange = noop }) {
  const intl = useIntl();
  const id = useId();

  const resolvedLabel = label ?? intl.formatMessage({ id: "checkboxField.label" });

  return (
    <label htmlFor={id} className="flex items-center gap-2">
      <input
        id={id}
        type="checkbox"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
        className="h-[13px] w-[13px] rounded-[3px] border border-[#CBD5E1] bg-white align-middle text-[#155DFC] focus:outline-none focus:ring-2 focus:ring-[#155DFC]/30"
      />
      <span className="text-base font-medium leading-6 tracking-[-0.3125px] text-[#4A5565]">
        {resolvedLabel}
      </span>
    </label>
  );
}