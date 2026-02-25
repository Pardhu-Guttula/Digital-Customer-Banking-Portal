import React, { useId } from "react";
import { useIntl } from "react-intl";
import { User } from "lucide-react";
import LabeledInput from "./LabeledInput";
import CheckboxWithLabel from "./CheckboxWithLabel";
import TextLink from "./TextLink";
import PrimaryButton from "./PrimaryButton";

export default function SignInCard({
  usernameOrEmail,
  password,
  rememberMe,
  loading = false,
  onUsernameOrEmailChange = () => {},
  onPasswordChange = () => {},
  onRememberMeChange = () => {},
  onForgotPassword = () => {},
  onSubmit = () => {},
}) {
  const intl = useIntl();

  const usernameId = useId();
  const passwordId = useId();
  const rememberId = useId();

  return (
    <section
      aria-label="Sign in"
      className="w-full max-w-[448px] rounded-[14px] border border-[#e5e7eb] bg-white shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]"
    >
      <div className="px-6 pt-6">
        <div className="flex items-center gap-1.5">
          <User aria-hidden="true" className="h-5 w-5 text-[#0a0a0a]" />
          <h2 className="text-[16px] leading-4 font-medium tracking-[-0.3125px] text-[#0a0a0a]">
            {intl.formatMessage({ id: "signInCard.title" })}
          </h2>
        </div>

        <p className="mt-3 text-[16px] leading-6 tracking-[-0.3125px] text-[#717182]">
          {intl.formatMessage({ id: "signInCard.description" })}
        </p>
      </div>

      <form
        className="px-6 pb-6 pt-4 flex flex-col gap-4"
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit({ usernameOrEmail, password, rememberMe });
        }}
      >
        <LabeledInput
          id={usernameId}
          label={intl.formatMessage({ id: "signInCard.usernameOrEmailLabel" })}
          type="text"
          value={usernameOrEmail}
          onChange={onUsernameOrEmailChange}
          placeholder={intl.formatMessage({ id: "signInCard.usernameOrEmailPlaceholder" })}
          autoComplete="username"
        />

        <LabeledInput
          id={passwordId}
          label={intl.formatMessage({ id: "signInCard.passwordLabel" })}
          type="password"
          value={password}
          onChange={onPasswordChange}
          placeholder={intl.formatMessage({ id: "signInCard.passwordPlaceholder" })}
          autoComplete="current-password"
        />

        <div className="flex items-center justify-between gap-4">
          <CheckboxWithLabel
            id={rememberId}
            checked={rememberMe}
            onCheckedChange={onRememberMeChange}
            label={intl.formatMessage({ id: "signInCard.rememberMe" })}
          />

          <TextLink onClick={onForgotPassword} href="#forgot-password">
            {intl.formatMessage({ id: "signInCard.forgotPassword" })}
          </TextLink>
        </div>

        <PrimaryButton type="submit" disabled={loading}>
          {loading
            ? intl.formatMessage({ id: "signInCard.continuing" })
            : intl.formatMessage({ id: "signInCard.continue" })}
        </PrimaryButton>
      </form>
    </section>
  );
}