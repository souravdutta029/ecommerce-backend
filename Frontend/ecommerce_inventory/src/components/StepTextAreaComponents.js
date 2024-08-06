import { Box, FormControl, FormControlLabel, InputLabel, MenuItem, Select, Switch, TextField } from '@mui/material';
import { useFormContext } from 'react-hook-form';

const StepTextAreaComponents = ({formConfig, fieldType}) => {
    const {register, formState: {errors}} = useFormContext();
    const textAreaFields = formConfig.data.textarea
    return (
        <Box>
            {textAreaFields.map((field, index) => (
                <TextField 
                fullWidth
                margin='normal'
                key={field.name}
                label={field.label}
                error={!!errors[field.name]}
                defaultValue={field.default}
                placeholder={field.placeholder}
                rows={4}
                multiline
                {...register(field.name, {required:field.required})}
                />
            ))}
        </Box>
    )
}

export default StepTextAreaComponents